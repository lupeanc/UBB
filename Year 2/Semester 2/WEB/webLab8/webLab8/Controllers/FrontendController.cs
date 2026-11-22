using Microsoft.AspNetCore.Mvc;
using webLab8.DataAbstractionLayer;

namespace webLab8.Controllers
{
    [ApiController]
    [Route("")]
    public class FrontendController : ControllerBase
    {
        // create a new data abstraction layer obj for db
        private readonly DAL dal = new DAL();

        [HttpGet]
        // read the 'action' query from the url to determine which method to call
        public IActionResult Handle([FromQuery(Name = "action")] string? actionName)
        {
            return actionName switch
            {
                "getUser" => Login(),
                "getAllReservations" => Ok(dal.GetAllReservations()),
                "getAllRooms" => Ok(dal.GetAllRooms()),
                "getReservation" => GetReservation(),
                "getRoom" => GetRoom(),
                "getNbBeds" => Ok(dal.GetNbBeds()),
                "getCategories" => Ok(dal.GetCategories()),
                "getPrices" => Ok(dal.GetPrices()),
                "getFilteredRoomsByNbBeds" => FilterByNbBeds(),
                "getFilteredRoomsByCategory" => FilterByCategory(),
                "getFilteredRoomsByPrice" => FilterByPrice(),
                "addReservation" => SaveResult(AddReservation()),
                "updateReservation" => SaveResult(UpdateReservation()),
                "deleteReservation" => SaveResult(DeleteReservation()),
                _ => BadRequest(new { result = "Error" })
            };
        }

        private IActionResult Login()
        {
            string username = QueryStringValue("username");
            string password = QueryStringValue("password");

            return SaveResult(dal.login(username, password));
        }

        private IActionResult GetReservation()
        {
            // tries to parse the 'id' query parameter from the url, if it fails, returns a bad request response
            // cool little syntax: if the id is in fact a valid int,
            // the function TryQueryInt will return true and the parsed value will be stored in the variable 'id'
            //
            // this should never return false/bad response since the id is filled in with data
            // already present in the database
            if (!TryQueryInt("id", out int id))
            {
                return BadRequest(new { result = "Error" });
            }

            var reservation = dal.GetReservation(id);
            // sends an ok status response if the reservation is found
            return reservation == null ? NotFound(new { result = "Error" }) : Ok(reservation);
        }

        private IActionResult GetRoom()
        {
            if (!TryQueryInt("id", out int id))
            {
                return BadRequest(new { result = "Error" });
            }

            var room = dal.GetRoom(id);
            return room == null ? NotFound(new { result = "Error" }) : Ok(room);
        }

        private IActionResult FilterByNbBeds()
        {
            return TryQueryInt("nb_beds", out int nbBeds)
                ? Ok(dal.GetFilteredRoomsByNbBeds(nbBeds))
                : BadRequest(new { result = "Error" });
        }

        private IActionResult FilterByCategory()
        {
            return Ok(dal.GetFilteredRoomsByCategory(QueryStringValue("category")));
        }

        private IActionResult FilterByPrice()
        {
            return TryQueryDecimal("price", out decimal price)
                ? Ok(dal.GetFilteredRoomsByPrice(price))
                : BadRequest(new { result = "Error" });
        }

        private bool AddReservation()
        {
            if (!TryReservationQuery(out int userId, out int roomId, out string start, out string end))
            {
                return false;
            }

            return dal.AddReservation(userId, roomId, start, end);
        }

        private bool UpdateReservation()
        {
            if (!TryQueryInt("id", out int id) ||
                !TryReservationQuery(out int userId, out int roomId, out string start, out string end))
            {
                return false;
            }

            return dal.UpdateReservation(id, userId, roomId, start, end);
        }

        private bool DeleteReservation()
        {
            return TryQueryInt("id", out int id) && dal.DeleteReservation(id);
        }

        // --- HELPER METHODS ===

        // returns an ok response with a json
        // structured like php: { "result": "OK" } or { "result": "Error" }
        private IActionResult SaveResult(bool success)
        {
            return Ok(new { result = success ? "OK" : "Error" });
        }

        // check if the url is correct for adding/updating a reservation
        // user_id, room_id are parsed, start and end are checked for being non empty
        private bool TryReservationQuery(out int userId, out int roomId, out string start, out string end)
        {
            userId = 0;
            roomId = 0;
            start = QueryStringValue("start");
            end = QueryStringValue("end");

            return TryQueryInt("user_id", out userId) &&
                   TryQueryInt("room_id", out roomId) &&
                   !string.IsNullOrWhiteSpace(start) &&
                   !string.IsNullOrWhiteSpace(end);
        }
        private bool TryQueryInt(string name, out int value)
        {
            return int.TryParse(QueryStringValue(name), out value);
        }

        private bool TryQueryDecimal(string name, out decimal value)
        {
            return decimal.TryParse(QueryStringValue(name), out value);
        }

        // !!!
        // tries to get value of "name" ("&name=5" => value=5)
        // if there is no value after "name"/"name" is not in the url
        // it returns an empty string
        private string QueryStringValue(string name)
        {
            return Request.Query.TryGetValue(name, out var value) ? value.ToString() : string.Empty;
        }
    }
}

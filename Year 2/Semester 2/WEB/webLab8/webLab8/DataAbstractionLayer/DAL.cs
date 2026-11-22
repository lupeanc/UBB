using MySql.Data.MySqlClient;
using webLab8.Models;

namespace webLab8.DataAbstractionLayer
{
    public class DAL
    {
        private static readonly List<User> Users = new List<User>();
        private static readonly List<Room> Rooms = new List<Room>();
        private static readonly List<Reservation> Reservations = new List<Reservation>();

        public MySqlConnection getConnection()
        {
            string myConnectionString = "Server=localhost;Database=web_lab5;Uid=root;Pwd=";
            return new MySqlConnection(myConnectionString);
        }

        public bool login(string username, string password)
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand(
                    "SELECT COUNT(*) FROM users WHERE username = @username AND password = @password",
                    conn);

                cmd.Parameters.AddWithValue("@username", username);
                cmd.Parameters.AddWithValue("@password", password);

                // check count. if different than 0, return false
                return Convert.ToInt32(cmd.ExecuteScalar()) == 1;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return false;
            }
        }

        public List<Reservation> GetAllReservations()
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand("SELECT id, user_id, room_id, `start`, `end` FROM reservations", conn);
                using MySqlDataReader reader = cmd.ExecuteReader();

                List<Reservation> reservations = new List<Reservation>();
                while (reader.Read())
                {
                    reservations.Add(ReadReservation(reader));
                }

                return reservations;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return Reservations;
            }
        }

        public Reservation? GetReservation(int id)
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand("SELECT id, user_id, room_id, `start`, `end` FROM reservations WHERE id = @id", conn);
                cmd.Parameters.AddWithValue("@id", id);

                using MySqlDataReader reader = cmd.ExecuteReader();
                return reader.Read() ? ReadReservation(reader) : null;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return Reservations.FirstOrDefault(r => r.Id == id);
            }
        }

        public List<Room> GetAllRooms()
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand("SELECT id, nb_beds, category, price FROM rooms", conn);
                using MySqlDataReader reader = cmd.ExecuteReader();

                List<Room> rooms = new List<Room>();
                while (reader.Read())
                {
                    rooms.Add(ReadRoom(reader));
                }

                return rooms;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return Rooms;
            }
        }

        public Room? GetRoom(int id)
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand("SELECT id, nb_beds, category, price FROM rooms WHERE id = @id", conn);
                cmd.Parameters.AddWithValue("@id", id);

                using MySqlDataReader reader = cmd.ExecuteReader();
                return reader.Read() ? ReadRoom(reader) : null;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return Rooms.FirstOrDefault(r => r.Id == id);
            }
        }

        public List<int> GetNbBeds()
        {
            return GetAllRooms().Select(r => r.NbBeds).Distinct().OrderBy(n => n).ToList();
        }

        public List<string> GetCategories()
        {
            return GetAllRooms().Select(r => r.Category).Distinct().OrderBy(c => c).ToList();
        }

        public List<decimal> GetPrices()
        {
            return GetAllRooms().Select(r => r.Price).Distinct().OrderBy(p => p).ToList();
        }

        public List<Room> GetFilteredRoomsByNbBeds(int nbBeds)
        {
            return GetAllRooms().Where(r => r.NbBeds == nbBeds).ToList();
        }

        public List<Room> GetFilteredRoomsByCategory(string category)
        {
            return GetAllRooms()
                // we are comparing 2 strings
                .Where(r => string.Equals(r.Category, category, StringComparison.OrdinalIgnoreCase))
                .ToList();
        }

        public List<Room> GetFilteredRoomsByPrice(decimal price)
        {
            return GetAllRooms().Where(r => r.Price <= price).ToList();
        }

        public bool AddReservation(int userId, int roomId, string start, string end)
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand(
                    "INSERT INTO reservations (user_id, room_id, `start`, `end`) VALUES (@userId, @roomId, @start, @end)",
                    conn);
                AddReservationParameters(cmd, userId, roomId, start, end);
                return cmd.ExecuteNonQuery() == 1;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return false;
            }
        }

        public bool UpdateReservation(int id, int userId, int roomId, string start, string end)
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand(
                    "UPDATE reservations SET user_id = @userId, room_id = @roomId, `start` = @start, `end` = @end WHERE id = @id",
                    conn);
                cmd.Parameters.AddWithValue("@id", id);
                AddReservationParameters(cmd, userId, roomId, start, end);
                return cmd.ExecuteNonQuery() == 1;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return false;
            }
        }

        public bool DeleteReservation(int id)
        {
            try
            {
                using MySqlConnection conn = getConnection();
                conn.Open();

                using MySqlCommand cmd = new MySqlCommand("DELETE FROM reservations WHERE id = @id", conn);
                cmd.Parameters.AddWithValue("@id", id);
                return cmd.ExecuteNonQuery() == 1;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return false;
            }
        }

        private static void AddReservationParameters(MySqlCommand cmd, int userId, int roomId, string start, string end)
        {
            cmd.Parameters.AddWithValue("@userId", userId);
            cmd.Parameters.AddWithValue("@roomId", roomId);
            cmd.Parameters.AddWithValue("@start", start);
            cmd.Parameters.AddWithValue("@end", end);
        }

        private static Reservation ReadReservation(MySqlDataReader reader)
        {
            return new Reservation(
                Convert.ToInt32(reader["id"]),
                Convert.ToInt32(reader["user_id"]),
                Convert.ToInt32(reader["room_id"]),
                FormatDate(reader["start"]),
                FormatDate(reader["end"]));
        }

        private static Room ReadRoom(MySqlDataReader reader)
        {
            return new Room(
                Convert.ToInt32(reader["id"]),
                Convert.ToInt32(reader["nb_beds"]),
                Convert.ToString(reader["category"]) ?? string.Empty,
                Convert.ToDecimal(reader["price"]));
        }

        private static string FormatDate(object value)
        {
            return value is DateTime date ? date.ToString("yyyy-MM-dd") : Convert.ToString(value) ?? string.Empty;
        }

    }
}

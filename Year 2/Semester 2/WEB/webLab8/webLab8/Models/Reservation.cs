using System.Text.Json.Serialization;

namespace webLab8.Models
{
    public class Reservation
    {
        [JsonPropertyName("id")]
        public int Id { get; }

        [JsonPropertyName("user_id")]
        public int UserId { get; set; }

        [JsonPropertyName("room_id")]
        public int RoomId { get; set; }

        [JsonPropertyName("start")]
        public string Start { get; set; }

        [JsonPropertyName("end")]
        public string End { get; set; }

        public Reservation(int id, int userId, int roomId, string start, string end)
        {
            this.Id = id;
            this.UserId = userId;
            this.RoomId = roomId;
            this.Start = start;
            this.End = end;
        }
    }
}

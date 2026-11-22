using System.Text.Json.Serialization;

namespace webLab8.Models
{
    // C# : pascal case, json : snake case so i have to spell it out for asp.net
    public class User
    {
        [JsonPropertyName("id")]
        public int Id { get; }

        [JsonPropertyName("username")]
        public string Username { get; set; }

        [JsonPropertyName("password")]
        public string Password { get; set; }

        public User(int id, string username, string password)
        {
            this.Id = id;
            this.Username = username;
            this.Password = password;
        }
    }
}

using System.Text.Json.Serialization;

namespace webLab8.Models
{
    public class Room
    {
        [JsonPropertyName("id")]
        public int Id { get; }

        [JsonPropertyName("nb_beds")]
        public int NbBeds { get; set; }

        [JsonPropertyName("category")]
        public string Category { get; set; }

        [JsonPropertyName("price")]
        public decimal Price { get; set; }

        public Room(int id, int nbBeds, string category, decimal price)
        {
            this.Id = id;
            this.NbBeds = nbBeds;
            this.Category = category;
            this.Price = price;
        }
    }
}

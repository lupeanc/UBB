using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;


namespace lab1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string connectionString = "Data Source=CUMPOOTER-THE-S\\SQLEXPRESS;" + "Initial Catalog=VideoGames; Integrated Security=true;";

            SqlConnection con = new SqlConnection(connectionString);

            con.Open();

            //Console.WriteLine("Connection opened successfully.");

            //SQL command
            string sqlCommStr = "SELECT * FROM Games";
            SqlCommand sqlComm = new SqlCommand(sqlCommStr, con);

            SqlDataAdapter daGames = new SqlDataAdapter(sqlCommStr, con);
            DataSet dsGames = new DataSet();

            daGames.Fill(dsGames, "Games");
            foreach (DataRow row in dsGames.Tables["Games"].Rows)
            {
                Console.WriteLine(row["gid"] + " " + row["gname"] + " " + row["grid"]);
            }
        }
    }
}

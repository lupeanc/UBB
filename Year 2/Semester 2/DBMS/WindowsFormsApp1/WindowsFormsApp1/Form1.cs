using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        SqlConnection con;
        SqlDataAdapter daGames;
        SqlDataAdapter daPublishers;
        DataSet ds;
        //BindingSource bsGames;
        //BindingSource bsPublishers;

        SqlCommandBuilder cmdBuilder;

        string queryGames;
        string queryPublishers;

        public Form1()
        {
            InitializeComponent();
            FillData();
        }

        void FillData()
        {
            string connectionString = "Data Source=CUMPOOTER-THE-S\\SQLEXPRESS;" + "Initial Catalog=VideoGames; Integrated Security=true;";

            con = new SqlConnection(connectionString);

            queryGames = "SELECT * FROM Games";
            queryPublishers = "SELECT * FROM Publishers";

            daGames = new SqlDataAdapter(queryGames, con);
            daPublishers = new SqlDataAdapter(queryPublishers, con);
            ds = new DataSet();
            daGames.Fill(ds, "Games");
            daPublishers.Fill(ds, "Publishers");

            cmdBuilder = new SqlCommandBuilder(daGames);

            ds.Relations.Add("GamesPublishers",
                ds.Tables["Publishers"].Columns["pubid"],
                ds.Tables["Games"].Columns["pubid"]);

            this.dataGridView1.DataSource = ds.Tables["Publishers"];
            this.dataGridView2.DataSource = this.dataGridView1.DataSource;
            this.dataGridView2.DataMember = "GamesPublishers";

            cmdBuilder.GetUpdateCommand();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //daGames.Update(ds, "Games");
            this.daGames.UpdateCommand = new SqlCommand("UPDATE Games SET gname=@gname, gyear=@gyear, pubid=@pubid, mrid=@mrid, grid=@grid WHERE gid=@gid", con);
            this.daGames.UpdateCommand.Parameters.Add("@gid", SqlDbType.Int).Value = Int32.Parse(textBox12.Text);
            if (textBox11.Text != "")
                this.daGames.UpdateCommand.Parameters.Add("@gname", SqlDbType.VarChar).Value = textBox11.Text;

            if (textBox10.Text != "")
                this.daGames.UpdateCommand.Parameters.Add("@gyear", SqlDbType.Int).Value = Int32.Parse(textBox10.Text);
            if (textBox9.Text != "")
                this.daGames.UpdateCommand.Parameters.Add("@pubid", SqlDbType.Int).Value = Int32.Parse(textBox9.Text);

            this.daGames.UpdateCommand.Parameters.Add("@mrid", SqlDbType.Int).Value = Int32.Parse(textBox8.Text);
            this.daGames.UpdateCommand.Parameters.Add("@grid", SqlDbType.Int).Value = Int32.Parse(textBox7.Text);

            this.con.Open();
            this.daGames.UpdateCommand.ExecuteNonQuery();
            this.con.Close();

            this.ds = new DataSet();
            this.daGames.Fill(this.ds, "Games");
            this.dataGridView2.DataSource = this.ds.Tables["Games"];

            this.textBox12.Clear();
            this.textBox11.Clear();
            this.textBox10.Clear();
            this.textBox9.Clear();
            this.textBox8.Clear();
            this.textBox7.Clear();
        }

        //ADD
        private void button2_Click(object sender, EventArgs e)
        {
            this.daGames.InsertCommand = new SqlCommand("INSERT INTO Games (gname, gyear, pubid, mrid, grid) VALUES (@gname, @gyear, @pubid, @mrid, @grid)", con);
            this.daGames.InsertCommand.Parameters.Add("@gname", SqlDbType.VarChar).Value=textBox1.Text;
            this.daGames.InsertCommand.Parameters.Add("@gyear", SqlDbType.Int).Value=Int32.Parse(textBox2.Text);
            this.daGames.InsertCommand.Parameters.Add("@pubid", SqlDbType.Int).Value=Int32.Parse(textBox3.Text);
            this.daGames.InsertCommand.Parameters.Add("@mrid", SqlDbType.Int).Value=Int32.Parse(textBox4.Text);
            this.daGames.InsertCommand.Parameters.Add("@grid", SqlDbType.Int).Value=Int32.Parse(textBox5.Text);

            this.con.Open();
            this.daGames.InsertCommand.ExecuteNonQuery();
            this.con.Close();

            this.ds = new DataSet();
            this.daGames.Fill(this.ds, "Games");
            this.dataGridView2.DataSource = this.ds.Tables["Games"];

            this.textBox1.Clear();
            this.textBox2.Clear();
            this.textBox3.Clear();
            this.textBox4.Clear();
            this.textBox5.Clear();
          
        }

        //REMOVE
        private void button3_Click(object sender, EventArgs e)
        {
            this.daGames.DeleteCommand = new SqlCommand("DELETE FROM Games WHERE gid = @gid", con);
            this.daGames.DeleteCommand.Parameters.Add("@gid", SqlDbType.Int).Value = Int32.Parse(textBox6.Text);

            this.con.Open();
            this.daGames.DeleteCommand.ExecuteNonQuery();
            this.con.Close();

            this.ds = new DataSet();
            this.daGames.Fill(this.ds, "Games");
            this.dataGridView2.DataSource = this.ds.Tables["Games"];

            this.textBox6.Clear();

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }
    }
}

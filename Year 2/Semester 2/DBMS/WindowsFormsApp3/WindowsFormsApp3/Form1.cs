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

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        SqlConnection conn;
        SqlDataAdapter daUsers, daPosts;
        SqlCommandBuilder cbPosts;
        DataSet ds;
        BindingSource bsUsers, bsPosts;
        public Form1()
        {
            InitializeComponent();
            this.Load += Form1_Load;

            btnSavePosts.Click += btnSavePosts_Click;
            btnRefresh.Click += btnRefresh_Click;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            conn = new SqlConnection(
                "Data Source=CUMPOOTER-THE-S\\SQLEXPRESS;Initial Catalog=dbms_s6;Integrated Security=True;"
            );

            daUsers = new SqlDataAdapter("SELECT * FROM Users", conn);
            daPosts = new SqlDataAdapter("SELECT * FROM Posts", conn);

            cbPosts = new SqlCommandBuilder(daPosts);
            daPosts.MissingSchemaAction = MissingSchemaAction.AddWithKey;

            ds = new DataSet();

            daUsers.Fill(ds, "Users");
            daPosts.Fill(ds, "Posts");

            DataRelation dr = new DataRelation(
                "FK_Posts_Users",
                ds.Tables["Users"].Columns["id"],
                ds.Tables["Posts"].Columns["uid"]
            );

            ds.Relations.Add(dr);

            bsUsers = new BindingSource();
            bsUsers.DataSource = ds;
            bsUsers.DataMember = "Users";

            bsPosts = new BindingSource();
            bsPosts.DataSource = bsUsers;
            bsPosts.DataMember = "FK_Posts_Users";

            dgvUsers.DataSource = bsUsers;
            dgvPosts.DataSource = bsPosts;
        }

        private void btnRefresh_Click(object sender, EventArgs e)
        {
            ds.Tables["Posts"].Clear();
            daPosts.Fill(ds, "Posts");
        }

        private void btnSavePosts_Click(object sender, EventArgs e)
        {
            daPosts.Update(ds, "Posts");
        }


    }
}

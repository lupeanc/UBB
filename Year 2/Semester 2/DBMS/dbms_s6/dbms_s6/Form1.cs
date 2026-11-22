using System;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace dbms_s6
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
            LoadData();
        }

        private void LoadData()
        {
            conn = new SqlConnection(
                "Data Source=DESKTOP-S6C1A6M;Initial Catalog=MiniFacebook;Integrated Security=SSPI"
            );

            daUsers = new SqlDataAdapter("SELECT * FROM Users", conn);
            daPosts = new SqlDataAdapter("SELECT * FROM Posts", conn);

            daPosts.MissingSchemaAction = MissingSchemaAction.AddWithKey;
            cbPosts = new SqlCommandBuilder(daPosts);

            ds = new DataSet();

            daUsers.Fill(ds, "Users");
            daPosts.Fill(ds, "Posts");

            DataRelation relation = new DataRelation(
                "Users_Posts",
                ds.Tables["Users"].Columns["UserID"],
                ds.Tables["Posts"].Columns["UserID"]
            );

            ds.Relations.Add(relation);

            bsUsers = new BindingSource();
            bsUsers.DataSource = ds;
            bsUsers.DataMember = "Users";

            bsPosts = new BindingSource();
            bsPosts.DataSource = bsUsers;
            bsPosts.DataMember = "Users_Posts";

            dgvUsers.DataSource = bsUsers;
            dgvPosts.DataSource = bsPosts;

            dgvPosts.AllowUserToAddRows = true;
            dgvPosts.AllowUserToDeleteRows = true;
            dgvPosts.ReadOnly = false;
        }

        private void btnSavePosts_Click(object sender, EventArgs e)
        {
            try
            {
                Validate();
                bsPosts.EndEdit();

                daPosts.Update(ds, "Posts");

                MessageBox.Show("Posts saved successfully.");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
        }
    }
}
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

namespace practicdbms
{
    public partial class Form1 : Form
    {
        SqlConnection conn;
        SqlDataAdapter daNeighborhoods, daSmartHomes;
        SqlCommandBuilder cbSmartHomes;
        DataSet ds;
        BindingSource bsNeighborhoods, bsSmartHomes;
        public Form1()
        {
            InitializeComponent();
            this.Load += Form1_Load;

            btnSave.Click += btnSave_Click;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            conn = new SqlConnection(
                "Data Source=CUMPOOTER-THE-S\\SQLEXPRESS;Initial Catalog=practicdbms;Integrated Security=True;"
            );

            daNeighborhoods = new SqlDataAdapter("SELECT * FROM Neighborhood", conn);
            daSmartHomes = new SqlDataAdapter("SELECT * FROM SmartHomes", conn);

            cbSmartHomes = new SqlCommandBuilder(daSmartHomes);
            daSmartHomes.MissingSchemaAction = MissingSchemaAction.AddWithKey;
            ds = new DataSet();

            daNeighborhoods.Fill(ds, "Neighborhood");
            daSmartHomes.Fill(ds, "SmartHomes");

            DataRelation dr = new DataRelation(
                "FK_SmartHomes_Neighborhoods",
                ds.Tables["Neighborhood"].Columns["id"],
                ds.Tables["SmartHomes"].Columns["nid"]
            );

            ds.Relations.Add(dr);

            bsNeighborhoods = new BindingSource();
            bsNeighborhoods.DataSource = ds;
            bsNeighborhoods.DataMember = "Neighborhood";

            bsSmartHomes = new BindingSource();
            bsSmartHomes.DataSource = bsNeighborhoods;
            bsSmartHomes.DataMember = "FK_SmartHomes_Neighborhoods";
            dgvNeighborhoods.DataSource = bsNeighborhoods;
            dgvSmartHomes.DataSource = bsSmartHomes;
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            daSmartHomes.Update(ds, "SmartHomes");
        }
    }
    }

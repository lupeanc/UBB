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

namespace CofShop2
{
    public partial class Form1 : Form
    {
        SqlConnection conn;
        SqlDataAdapter daCoffeeShops, daEmployers;
        SqlCommandBuilder cbEmployers;
        DataSet ds;
        BindingSource bsCoffeeShops, bsEmployers;
        public Form1()
        {
            InitializeComponent();
            this.Load += Form1_Load;

            btnSave.Click += btnSave_Click;
            btnRefresh.Click += btnRefresh_Click;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            conn = new SqlConnection(
                "Data Source=CUMPOOTER-THE-S\\SQLEXPRESS;Initial Catalog=CoffeeShopDBMS;Integrated Security=True;"
            );

            daCoffeeShops = new SqlDataAdapter("SELECT * FROM CoffeeShops", conn);
            daEmployers = new SqlDataAdapter("SELECT * FROM Employers", conn);

            cbEmployers = new SqlCommandBuilder(daEmployers);
            daEmployers.MissingSchemaAction = MissingSchemaAction.AddWithKey;
            ds = new DataSet();

            daCoffeeShops.Fill(ds, "CoffeeShops");
            daEmployers.Fill(ds, "Employers");

            DataRelation dr = new DataRelation(
                "FK_Employers_CoffeeShops",
                ds.Tables["CoffeeShops"].Columns["id"],
                ds.Tables["Employers"].Columns["csid"]
            );

            ds.Relations.Add(dr);

            bsCoffeeShops = new BindingSource();
            bsCoffeeShops.DataSource = ds;
            bsCoffeeShops.DataMember = "CoffeeShops";

            bsEmployers = new BindingSource();
            bsEmployers.DataSource = bsCoffeeShops;
            bsEmployers.DataMember = "FK_Employers_CoffeeShops";

            dgvCoffeeShops.DataSource = bsCoffeeShops;
            dgvEmployers.DataSource = bsEmployers;
        }

        private void btnRefresh_Click(object sender, EventArgs e)
        {
            ds.Tables["Employers"].Clear();
            daEmployers.Fill(ds, "Employers");
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            daEmployers.Update(ds, "Employers");
        }
    }
}

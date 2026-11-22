namespace CofShop2
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dgvCoffeeShops = new System.Windows.Forms.DataGridView();
            this.dgvEmployers = new System.Windows.Forms.DataGridView();
            this.btnSave = new System.Windows.Forms.Button();
            this.btnRefresh = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCoffeeShops)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvEmployers)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvCoffeeShops
            // 
            this.dgvCoffeeShops.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvCoffeeShops.Location = new System.Drawing.Point(23, 22);
            this.dgvCoffeeShops.Name = "dgvCoffeeShops";
            this.dgvCoffeeShops.RowHeadersWidth = 51;
            this.dgvCoffeeShops.RowTemplate.Height = 24;
            this.dgvCoffeeShops.Size = new System.Drawing.Size(530, 306);
            this.dgvCoffeeShops.TabIndex = 0;
            // 
            // dgvEmployers
            // 
            this.dgvEmployers.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvEmployers.Location = new System.Drawing.Point(635, 23);
            this.dgvEmployers.Name = "dgvEmployers";
            this.dgvEmployers.RowHeadersWidth = 51;
            this.dgvEmployers.RowTemplate.Height = 24;
            this.dgvEmployers.Size = new System.Drawing.Size(544, 305);
            this.dgvEmployers.TabIndex = 1;
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(189, 375);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(215, 70);
            this.btnSave.TabIndex = 2;
            this.btnSave.Text = "Save";
            this.btnSave.UseVisualStyleBackColor = true;
            // 
            // btnRefresh
            // 
            this.btnRefresh.Location = new System.Drawing.Point(807, 375);
            this.btnRefresh.Name = "btnRefresh";
            this.btnRefresh.Size = new System.Drawing.Size(218, 70);
            this.btnRefresh.TabIndex = 3;
            this.btnRefresh.Text = "Refresh";
            this.btnRefresh.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1191, 527);
            this.Controls.Add(this.btnRefresh);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.dgvEmployers);
            this.Controls.Add(this.dgvCoffeeShops);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dgvCoffeeShops)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvEmployers)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvCoffeeShops;
        private System.Windows.Forms.DataGridView dgvEmployers;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Button btnRefresh;
    }
}


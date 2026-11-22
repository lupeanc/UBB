namespace practicdbms
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
            this.dgvNeighborhoods = new System.Windows.Forms.DataGridView();
            this.dgvSmartHomes = new System.Windows.Forms.DataGridView();
            this.btnSave = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dgvNeighborhoods)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvSmartHomes)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvNeighborhoods
            // 
            this.dgvNeighborhoods.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvNeighborhoods.Location = new System.Drawing.Point(31, 12);
            this.dgvNeighborhoods.Name = "dgvNeighborhoods";
            this.dgvNeighborhoods.RowHeadersWidth = 51;
            this.dgvNeighborhoods.RowTemplate.Height = 24;
            this.dgvNeighborhoods.Size = new System.Drawing.Size(469, 357);
            this.dgvNeighborhoods.TabIndex = 0;
            // 
            // dgvSmartHomes
            // 
            this.dgvSmartHomes.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvSmartHomes.Location = new System.Drawing.Point(535, 12);
            this.dgvSmartHomes.Name = "dgvSmartHomes";
            this.dgvSmartHomes.RowHeadersWidth = 51;
            this.dgvSmartHomes.RowTemplate.Height = 24;
            this.dgvSmartHomes.Size = new System.Drawing.Size(735, 357);
            this.dgvSmartHomes.TabIndex = 1;
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(336, 418);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(362, 96);
            this.btnSave.TabIndex = 2;
            this.btnSave.Text = "Save Changes";
            this.btnSave.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(221, 376);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(101, 16);
            this.label1.TabIndex = 3;
            this.label1.Text = "Neighborhoods";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(879, 376);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(86, 16);
            this.label2.TabIndex = 4;
            this.label2.Text = "SmartHomes";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1308, 671);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.dgvSmartHomes);
            this.Controls.Add(this.dgvNeighborhoods);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dgvNeighborhoods)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvSmartHomes)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvNeighborhoods;
        private System.Windows.Forms.DataGridView dgvSmartHomes;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
    }
}


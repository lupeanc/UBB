namespace lab2
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
            this.childTable = new System.Windows.Forms.DataGridView();
            this.parentTable = new System.Windows.Forms.DataGridView();
            this.insertButton = new System.Windows.Forms.Button();
            this.updateButton = new System.Windows.Forms.Button();
            this.deleteButton = new System.Windows.Forms.Button();
            this.panel = new System.Windows.Forms.Panel();
            ((System.ComponentModel.ISupportInitialize)(this.childTable)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.parentTable)).BeginInit();
            this.SuspendLayout();
            // 
            // childTable
            // 
            this.childTable.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.childTable.Location = new System.Drawing.Point(701, 35);
            this.childTable.Name = "childTable";
            this.childTable.RowHeadersWidth = 51;
            this.childTable.RowTemplate.Height = 24;
            this.childTable.Size = new System.Drawing.Size(580, 310);
            this.childTable.TabIndex = 1;
            // 
            // parentTable
            // 
            this.parentTable.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.parentTable.Location = new System.Drawing.Point(39, 35);
            this.parentTable.Name = "parentTable";
            this.parentTable.RowHeadersWidth = 51;
            this.parentTable.RowTemplate.Height = 24;
            this.parentTable.Size = new System.Drawing.Size(580, 310);
            this.parentTable.TabIndex = 2;
            // CHANGED FROM CellContentClick TO CellClick BECAUSE IT WASNT ALWAYS WORKING PROPERLY
            this.parentTable.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.parentTable_CellClick);
            // 
            // insertButton
            // 
            this.insertButton.Location = new System.Drawing.Point(244, 362);
            this.insertButton.Name = "insertButton";
            this.insertButton.Size = new System.Drawing.Size(128, 34);
            this.insertButton.TabIndex = 3;
            this.insertButton.Text = "insertButton";
            this.insertButton.UseVisualStyleBackColor = true;
            this.insertButton.Click += new System.EventHandler(this.insertButton_Click);
            // 
            // updateButton
            // 
            this.updateButton.Location = new System.Drawing.Point(588, 362);
            this.updateButton.Name = "updateButton";
            this.updateButton.Size = new System.Drawing.Size(128, 34);
            this.updateButton.TabIndex = 4;
            this.updateButton.Text = "updateButton";
            this.updateButton.UseVisualStyleBackColor = true;
            this.updateButton.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // deleteButton
            // 
            this.deleteButton.Location = new System.Drawing.Point(938, 362);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(128, 34);
            this.deleteButton.TabIndex = 5;
            this.deleteButton.Text = "deleteButton";
            this.deleteButton.UseVisualStyleBackColor = true;
            this.deleteButton.Click += new System.EventHandler(this.deleteButton_Click);
            // 
            // panel
            // 
            this.panel.Location = new System.Drawing.Point(76, 428);
            this.panel.Name = "panel";
            this.panel.Size = new System.Drawing.Size(1183, 231);
            this.panel.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1320, 695);
            this.Controls.Add(this.panel);
            this.Controls.Add(this.deleteButton);
            this.Controls.Add(this.updateButton);
            this.Controls.Add(this.insertButton);
            this.Controls.Add(this.parentTable);
            this.Controls.Add(this.childTable);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.childTable)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.parentTable)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView childTable;
        private System.Windows.Forms.DataGridView parentTable;
        private System.Windows.Forms.Button insertButton;
        private System.Windows.Forms.Button updateButton;
        private System.Windows.Forms.Button deleteButton;
        private System.Windows.Forms.Panel panel;
    }
}


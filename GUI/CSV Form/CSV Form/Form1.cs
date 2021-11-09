using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CSV_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                OpenFileDialog1.ShowDialog();
                string fn = OpenFileDialog.Filename;
                string readfile = File.ReadAllText(fn);
                string[] line = readfile.Split('\n');
                int count = 0;
                foreach (string str in line[0].Split(','))
                {
                    count++;
                }
                DataGridView1.ColumnCount = count;
                foreach (string s1 in readfile.Split('\n'))
                {
                    if (s1 != "")
                        DataGridview1.Rows.Add(s1.Split(','));
                }
            }
            catch (Exception)
            {
                MessageBox.Show("geen bestand");
            }





        }
        private void button2_Click(object sender, EventArgs e)
        {
            int rowcount = datagridview1.rowcount - 1;


        }
    }
}

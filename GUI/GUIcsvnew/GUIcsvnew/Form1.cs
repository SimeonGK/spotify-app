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

namespace GUIcsvnew
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
       
private void button1_Click_1(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.ShowDialog();
                string fn = openFileDialog1.FileName;
                string readfile = File.ReadAllText(fn);
                string[] line = readfile.Split('\n');
                int count = 0;
                foreach (string str in line[0].Split(','))
                {
                    count++;
                }
                dataGridView1.ColumnCount = count;  
                foreach (string s1 in readfile.Split('\n'))
                {
                    if (s1 != "")
                        dataGridView1.Rows.Add(s1.Split(','));

                }

            } catch (Exception)
            {
                MessageBox.Show("geen bestand, probeer het opnieuw");
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int rowcount = dataGridView1.RowCount - 1;
            double c1 = 0, c2 = 0;
            for (int i = 1; i < rowcount; i++)
            {
                c1 = Convert.ToDouble(dataGridView1.Rows[i].Cells[0].Value);
                c2 = Convert.ToDouble(dataGridView1.Rows[i].Cells[1].Value);
                chart1.Series["Series1"].Points.AddXY(c1, c2);
            }

        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }
    }
}

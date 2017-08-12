using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace PeoriaCity
{
    public partial class Construction : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            {
                string html = string.Empty;
                string fromStreet = txtStreetFrom.Text;
                string toStreet = txtStreetTo.Text;
                string key = "AIzaSyBhojUzlNBM8XhyQpjt3ggBa2vm1XRo_xo";
                //foreach (char chr in address)
                //{
                //    if (chr == ' ')
                //    {
                //        address[i] = "+";
                //    }
                //}
                string strCmdText;
                strCmdText = "/K python c:\\geocode\\geocode.py ";  //  fromStreet + " to " + toStreet;
                System.Diagnostics.Process.Start("CMD.exe", strCmdText);
                //string url = @"https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + key;

                //HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
                //request.AutomaticDecompression = DecompressionMethods.GZip;

                //using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
                //using (System.IO.Stream stream = response.GetResponseStream())
                //using (StreamReader reader = new StreamReader(stream))
                //{
                //    html = reader.ReadToEnd();
                //}

                //dynamic dynObj = JsonConvert.DeserializeObject(html);

                //// Console.WriteLine(html);
                ////Console.WriteLine("Latitude - " + dynObj.results[0].geometry.location.lat);
                ////Console.WriteLine("Longitude = " + dynObj.results[0].geometry.location.lng);

                //txtLng.Text = dynObj.results[0].geometry.location.lng;
                //txtLat.Text = dynObj.results[0].geometry.location.lat;
            }
        }
    }
}
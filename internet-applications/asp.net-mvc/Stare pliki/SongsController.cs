using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class SongsController : Controller
    {
        // GET: Songs
        public ActionResult Index()
        {
            Song song = new Song();
            song.Name = "I Am Mine";
            song.Artist = "Pearl Jam";
            song.Genre = "Alternative/Grunge";
            song.Id = 1;
            return View(song);
            // return Content("Hello World!");
        }

        public ActionResult Square(int id)
        {
            return Content((id * id).ToString());
        }
    }
}
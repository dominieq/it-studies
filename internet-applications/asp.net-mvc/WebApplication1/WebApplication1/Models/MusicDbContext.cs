using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace WebApplication1.Models
{
    public class MusicDbContext : DbContext
    {
        public MusicDbContext() : base("DefaultConnection") { }
        public DbSet<Song> Songs { get; set; }

        public System.Data.Entity.DbSet<WebApplication1.Models.Genre> Genres { get; set; }
    }
}
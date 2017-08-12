using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(PeoriaCity.Startup))]
namespace PeoriaCity
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}

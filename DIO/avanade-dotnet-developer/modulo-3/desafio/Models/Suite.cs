namespace SuiteModel
{
    public class Suite
    {
        public string TipoSuite { get; set; }
        public int Capacidade { get; set; }
        public decimal ValorDiaria { get; set; }

        public Suite()
        {
            TipoSuite = "normal";
        }
    }
}

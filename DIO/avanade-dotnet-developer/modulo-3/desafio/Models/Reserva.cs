using SuiteModel;
using PessoaModel;

namespace ReservaModel
{
    public class Reserva
    {
        private List<Pessoa> ListaPessoa { get; set; }
        private Suite SuiteReservada { get; set; }
        private int DiasReservados { get; set; }

        public Reserva()
        {
            ListaPessoa = new List<Pessoa>();
            SuiteReservada = new Suite();
        }

        public Reserva(List<Pessoa> lista, Suite suite, int dias)
        {
            ListaPessoa = lista;
            SuiteReservada = suite;
            DiasReservados = dias;
        }


        public void CadastrarHospedes(Pessoa hospede)
        {
            try
            {
                int QntPesssoasHospedadas = ListaPessoa.Count;
                int Capacidade = SuiteReservada.Capacidade;
                if (QntPesssoasHospedadas < Capacidade)
                {
                    ListaPessoa.Add(hospede);
                    Console.WriteLine("Hospede Cadastrado com sucesso!");
                }
                else
                {
                    Console.WriteLine($"A quantidade de Pessoas é maior que a quantidade de hospedes!\n Quantidade de pessoas: {QntPesssoasHospedadas}\n Capacidade da Reserva: {Capacidade}");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine($"Exceção ocorrida! {e}");
            }
        }

        public void CadastrarSuite(Suite suite)
        {
            SuiteReservada = suite;
        }

        public void ObterQuantidadeHospedes()
        {
            Console.WriteLine($"A quantidade de hospedes é: {ListaPessoa.Count}");
        }

        public void ReservarDias(int dias)
        {
            DiasReservados = dias;
        }

        public void CalcularValorDiaria()
        {
            Console.WriteLine($"{SuiteReservada.ValorDiaria.ToString("C")}, {DiasReservados}");
            Console.WriteLine($"O valor da diária é : {(SuiteReservada.ValorDiaria * DiasReservados).ToString("C")}");
        }

    }
}

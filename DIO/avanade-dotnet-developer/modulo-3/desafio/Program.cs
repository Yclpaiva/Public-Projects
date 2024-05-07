using PessoaModel;
using ReservaModel;
using SuiteModel;

Pessoa p1 = new Pessoa();
Pessoa p2 = new Pessoa();

Suite suiteNormal = new Suite();
suiteNormal.Capacidade = 1;
suiteNormal.ValorDiaria = 200M;

Suite suiteVIP = new Suite();
suiteVIP.Capacidade = 2;
suiteVIP.ValorDiaria = 500M;

List<Pessoa> casal = new List<Pessoa> { p1, p2 };

Reserva num001 = new Reserva();
num001.CadastrarSuite(suiteNormal);
num001.CadastrarHospedes(p1);
num001.ReservarDias(2);

Reserva num002 = new Reserva(casal, suiteVIP, 5);

num001.CalcularValorDiaria();
num002.CalcularValorDiaria();

List<string> listaVeiculos = new List<string>();
List<string> listaTempo = new List<string>();

while (true)
{
    Console.WriteLine("Bem vindo ao sistema de controle de estacionamento!\n\n");
    Console.WriteLine("Digite 1 para adicionar\n Digite 2 para remover\n Digite 3 para listar\n Digite 4 para sair\n\n");
    int opcao = Convert.ToInt32(Console.ReadLine());

    switch (opcao)
    {
        case 1:
            Console.WriteLine("Digite a placa do veículo: \n");
            listaVeiculos.Add(Console.ReadLine());
            Console.WriteLine("Digite o tempo em minutos que você vai ficar: \n");
            listaTempo.Add(Console.ReadLine());
            break;
        case 2:
            Console.WriteLine("Digite a placa do veículo: \n");
            for (int counter = 0; counter < listaVeiculos.Count; counter++)
            {
                if (listaVeiculos[counter] == Console.ReadLine())
                {
                    Console.WriteLine("Veículo encontrado! Pague o valor de R$" + (Convert.ToInt32(listaTempo[counter]) * 10).ToString("0.00"));
                    listaVeiculos.RemoveAt(counter);
                    listaTempo.RemoveAt(counter);
                }
                else
                {
                    Console.WriteLine("Veículo não encontrado \n");
                }

            }
            break;
        case 3:
            for (int counter = 0; counter < listaVeiculos.Count; counter++)
            {
                Console.WriteLine("---- Lista de Veículos ----");
                Console.WriteLine(listaVeiculos[counter] + "\n");
            }
            break;
        default:
        case 4:
            break;
    }
}

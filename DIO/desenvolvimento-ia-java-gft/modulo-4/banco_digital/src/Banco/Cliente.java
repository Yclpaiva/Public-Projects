package Banco;

import java.util.List;

public class Cliente {

    private double saldo;
    private String nome;
    private String cpf;
    private int numeroConta;
    private static int proximoNumeroConta = 1;
    private List<Historico> historicoList;

    public Cliente(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
        this.numeroConta = proximoNumeroConta++;
        this.saldo = 0;
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public String getNome() {
        return nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void depositar(double valor) {
        saldo += valor;
        Historico transacao = new Historico("Deposito", valor, String.valueOf(this.numeroConta), "Boca do caixa");
        historicoList.add(transacao);
    }

    public boolean deduzirSaldo(double valor) {
        if (valor > saldo) {
            return false;
        }else {
            saldo -= valor;
            return true;
        }
    }

    public void transferir(Cliente destinatario, double valor) {
        if (deduzirSaldo(valor)) {
            Historico transacao = new Historico("Saque", valor, String.valueOf(destinatario), String.valueOf(this.numeroConta));
            destinatario.depositar(valor);
            historicoList.add(transacao);
        } else {
            System.out.println("Transferência não realizada, saldo insuficiente");
        }
    }

    public void sacar(double valor){
        if(deduzirSaldo(valor)){
            System.out.println("Saque realizado com sucesso");
        }else {
            System.out.println("Saldo insuficiente");
        }
    }
}

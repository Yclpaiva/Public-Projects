package Banco;

public class Historico {

    private String descricao;
    private double valor;
    private String destinatario;
    private String remetente;

    public Historico(String descricao, double valor, String destinatario, String remetente) {
        this.descricao = descricao;
        this.valor = valor;
        this.destinatario = destinatario;
        this.remetente = remetente;
    }
}

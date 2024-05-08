SELECT Max(Preco) MaxPrecos FROM Produtos -- retorna o max dos produtos
SELECT Max(Preco) FROM Produtos WHERE Tamanho = 'M' -- retorna o max dos produtos que são do tamanho M
SELECT Min(Preco) MinPrecosF FROM Produtos WHERE Tamanho = 'F' -- retorna o mínimo dos produtos do tamanho F
SELECT AVG(Preco) AVGPrecos FROM Produtos -- retorna a média de todos os preços cadatrados na tabela sistema

SELECT Nome+'-'+Cor FROM Produtos; -- retorna as duas strings como Nome-Cor, concatena elas


SELECT * FROM Produtos;
ALTER TABLE Produtos;
ADD DataCadastro DATETIME2; -- adiciona uma coluna do tipo datetime2 na tabela Produtos

UPDATE Produtos SET DataCadastro = GETDATE(); -- atualiza a coluna DataCadastro com a data atual


ALTER TABLE Produtos
DROP COLUMN DataCadastro; -- remove a coluna DataCadastro da tabela Produtos

SELECT FORMAT(DataCadastro, 'dd/MM/yyyy') AS Data FROM Produtos;  -- formata a data para o padrão dd/MM/yyyy , o AS é opcional, funciona da mesma forma.

SELECT Tamanho, COUNT(*) Quantidade FROM Produtos WHERE Tamanho <> '' GROUP BY Tamanho; -- agrupa os produtos por tamanho e conta quantos produtos tem em cada grupo, e separa os que não tem tamanho

SELECT Tamanho, COUNT(*) Quantidade FROM Produtos WHERE Tamanho <> '' GROUP BY Tamanho HAVING COUNT(*) > 1; -- agrupa os produtos por tamanho e conta quantos produtos tem em cada grupo, e separa os que não tem tamanho, e só retorna os que tem mais de 1 produto

CREATE TABLE Enderecos(
    Id INT PRIMARY KEY IDENTITY(1,1),
    IdCliente int NULL,
    Rua VARCHAR(100) NOT NULL,
    Numero INT NOT NULL,
    Bairro VARCHAR(50) NOT NULL,
    Cidade VARCHAR(50) NOT NULL,
    Estado CHAR(2) NOT NULL,

    Constraint FK_Enderecos_Clientes FOREIGN KEY(IdCliente) REFERENCES Clientes(Id) -- cria uma chave estrangeira para a tabela Clientes, que referencia a coluna Id
)

SELECT * FROM Clientes
INNER JOIN Enderecos  ON Clientes.Id = Enderecos.IdCliente
WHERE Clientes.Id = 4 -- retorna os clientes que tem o id 4 e seus endereços, utilizando o método INNER JOINS

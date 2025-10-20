// Pega o botão e o local onde o conteúdo será inserido
const botao = document.getElementById('carregar-btn');
const divConteudo = document.getElementById('conteudo');
// Adiciona um evento para quando o botão for clicado
botao.addEventListener('click', () => {
// 1. O JavaScript pede os "ingredientes" para a API do servidor
fetch('/api/alunos')
.then(response => response.json()) // Converte a resposta para JSON
.then(dados_dos_alunos => {
// 2. O JavaScript MONTA o HTML aqui, no NAVEGADOR
let tabelaHTML = '<table border="1">';
tabelaHTML += `
<tr>
<th>Aluno</th>
<th>Nota</th>
</tr>
`;
// Cria uma linha para cada aluno que veio da API
for (const aluno of dados_dos_alunos) {
tabelaHTML += `
<tr>
<td>${aluno.nome}</td>
<td>${aluno.nota}</td>
</tr>
`;
}
tabelaHTML += '</table>';
// 3. Insere o HTML montado dentro da div "conteudo"
divConteudo.innerHTML = tabelaHTML;
});
});
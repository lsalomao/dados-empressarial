document.getElementById('searchButton').addEventListener('click', async () => {
    const cnpjInput = document.getElementById('cnpjInput').value;
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');

    // Limpa resultados anteriores
    resultDiv.classList.add('hidden');
    errorDiv.classList.add('hidden');
    resultDiv.innerHTML = '';
    errorDiv.innerHTML = '';

    // Valida o CNPJ (somente números, 14 dígitos)
    const cleanCnpj = cnpjInput.replace(/[^\d]/g, '');
    if (cleanCnpj.length !== 14) {
        errorDiv.classList.remove('hidden');
        errorDiv.innerHTML = 'Por favor, insira um CNPJ válido com 14 dígitos.';
        return;
    }

    try {
        const response = await fetch(`/api/cnpj/${cleanCnpj}`);
        if (!response.ok) {
            throw new Error((await response.json()).detail || 'Erro na consulta');
        }

        const data = await response.json();
        const sociosList = data.qsa.length > 0
        ? data.qsa.map(socio => `${socio.nome} (${socio.qual})`).join(', ')
        : 'Nenhum sócio registrado';

        resultDiv.classList.remove('hidden');
        resultDiv.innerHTML = `
            <h2 class="text-lg font-semibold">${data.nome}</h2>
            <p><strong>CNPJ:</strong> ${data.cnpj}</p>
            <p><strong>Data de Abertura:</strong> ${data.abertura}</p>
            <p><strong>Situação:</strong> ${data.situacao}</p>
            <p><strong>Sócios:</strong> ${sociosList}</p>
            <p><strong>Atividade Principal:</strong> ${data.atividade_principal[0]?.text || 'N/A'}</p>
            <p><strong>Endereço:</strong> ${data.logradouro}, ${data.numero}, ${data.bairro}, ${data.municipio} - ${data.uf}</p>
            <p><strong>Telefone:</strong> ${data.telefone || 'N/A'}</p>
            <p><strong>Email:</strong> ${data.email || 'N/A'}</p>
        `;
    } catch (error) {
        errorDiv.classList.remove('hidden');
        errorDiv.innerHTML = `Erro: ${error.message}`;
    }
});
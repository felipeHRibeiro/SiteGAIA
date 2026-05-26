let dadosGlobais = [];
                <div class="card-header">

                    <h3>${item.nome}</h3>

                    <p class="short-desc">
                        ${item.descricao}
                    </p>

                    <div class="actions">

                        <a href="${item.site}" target="_blank" class="btn-visit">
                            Visitar Site
                        </a>

                        <button class="btn-desc" onclick="toggleAccordion(this)">
                            Descrição
                        </button>

                    </div>

                </div>

                <div class="card-content">

                    <div class="info-grid">

                        <div class="info-item">
                            <strong>Instituição</strong>
                            <span>${item.instituicao}</span>
                        </div>

                        <div class="info-item">
                            <strong>País</strong>
                            <span>${item.pais}</span>
                        </div>

                        <div class="info-item">
                            <strong>Moeda</strong>
                            <span>${item.moeda}</span>
                        </div>

                        <div class="info-item">
                            <strong>Valor</strong>
                            <span>${item.valor}</span>
                        </div>

                        <div class="info-item">
                            <strong>Setor</strong>
                            <span>${item.setor}</span>
                        </div>

                    </div>

                </div>

            </div>
        `;
    });
}

function toggleAccordion(btn) {

    const card = btn.closest('.card');

    card.classList.toggle('active');
}

const filtro = document.getElementById('setor');

filtro.addEventListener('change', () => {

    const valor = filtro.value;

    if (valor === 'todos') {
        renderizarCards(dadosGlobais);
        return;
    }

    const filtrados = dadosGlobais.filter(item => item.setor === valor);

    renderizarCards(filtrados);
});
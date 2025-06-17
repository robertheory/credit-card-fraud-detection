document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('fraudForm');
  const resultDiv = document.getElementById('result');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    resultDiv.innerHTML = '';

    // Coleta os dados do formulário
    const data = {
      distance_from_home: parseFloat(form.distance_from_home.value),
      distance_from_last_transaction: parseFloat(form.distance_from_last_transaction.value),
      ratio_to_median_purchase_price: parseFloat(form.ratio_to_median_purchase_price.value),
      repeat_retailer: parseFloat(form.repeat_retailer.value),
      used_chip: parseFloat(form.used_chip.value),
      used_pin_number: parseFloat(form.used_pin_number.value),
      online_order: parseFloat(form.online_order.value)
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        throw new Error('Erro ao conectar com o servidor.');
      }

      const result = await response.json();

      // Espera que o backend retorne { "isFraud": true } ou { "isFraud": false }
      if (result.isFraud === true) {
        resultDiv.innerHTML = `
          <div class="alert alert-danger" role="alert">
            Fraude detectada!
          </div>
        `;
      } else if (result.isFraud === false) {
        resultDiv.innerHTML = `
          <div class="alert alert-success" role="alert">
            Transação legítima.
          </div>
        `;
      } else {
        resultDiv.innerHTML = `
          <div class="alert alert-warning" role="alert">
            Resposta inesperada do servidor.
          </div>
        `;
      }
    } catch (error) {
      resultDiv.innerHTML = `
        <div class="alert alert-danger" role="alert">
          Erro: ${error.message}
        </div>
      `;
    }
  });
});
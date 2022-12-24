export default {
  mapeia_vizinhos(celula) {
    let x = celula[0], y = celula[1]
    let celulasVizinhas = [
      [x - 1, y - 1],
      [x - 1, y],
      [x - 1, y + 1],
      [x, y - 1],
      [x, y + 1],
      [x + 1, y - 1],
      [x + 1, y],
      [x + 1, y + 1]
    ]
    return celulasVizinhas
  },

  mapeia_vizinhos_mutiplos(celulas) {
    let vizinhos = []
    for (let celula of celulas) {
      vizinhos.push(...this.mapeia_vizinhos(celula))
    }
    return vizinhos
  },

  contaOcorrenciaDeLista(listaDeListas, lista) {
    let ocorrencia = 0
    for (let array_ of listaDeListas) {
      if (array_[0] === lista[0] && array_[1] === lista[1]) {
        ocorrencia++
      }
    } return ocorrencia
  },

  validaListaNoArray(listaDeListas, lista) {
    for (let array_ of listaDeListas) {
      if (array_[0] === lista[0] && array_[1] === lista[1]) return true
    }
    return false
  },

  listasMutiplasOcorrencias(listaCelulasVizinhas, x) {
    let listasOcorrencias = []
    for (let lista of listaCelulasVizinhas) {
      let ocorrencia = this.contaOcorrenciaDeLista(listaCelulasVizinhas, lista)
      if (ocorrencia === x) {
        listasOcorrencias.push(lista)
      }
    }
    return this.removeRepeticao(listasOcorrencias)
  },

  removeRepeticao(listas) {
    let copiaLista = JSON.parse(JSON.stringify(listas))
    let novaLista = []
    for (let lista of copiaLista) {
      if (!this.validaListaNoArray(novaLista, lista)) {
        novaLista.push(lista)
      }
    } return novaLista
  },

  updateCelulasVivas(celulasAtivasAnteriores) {
    let celulasVizinhas = this.mapeia_vizinhos_mutiplos(celulasAtivasAnteriores)
    let celulasDuasVizinhasAtivas = this.listasMutiplasOcorrencias(celulasVizinhas, 2)
    let celulasTresVizinhasAtivas = this.listasMutiplasOcorrencias(celulasVizinhas, 3)
    let celulasAtivasDuasVizinhasAtivas = []
    for (let celula of celulasDuasVizinhasAtivas) {
      if (this.validaListaNoArray(celulasAtivasAnteriores, celula)) {
        celulasAtivasDuasVizinhasAtivas.push(celula)
      }
    } return [...celulasAtivasDuasVizinhasAtivas, ...celulasTresVizinhasAtivas]
  }
}
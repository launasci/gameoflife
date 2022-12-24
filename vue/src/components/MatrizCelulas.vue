<template>
  <div>
    <div v-for="linha in linhas" :key="linha" class="flex">
      <div v-for="coluna in colunas" :key="coluna">
        <CelulaStatus class="quadrado" :status-ativo="listaCelulasAtivas(linha, coluna)" />     
      </div>
    </div>
  </div>
</template>

<script>
import CelulaStatus from "./CelulaStatus";

export default {
  components: { CelulaStatus },
  props:{
    colunas:{
      type: Number,
      default: 0 
    },
    linhas:{
      type: Number,
      default: 0
    },
    celulasAtivas:{
      type:Array,
      default: () => []
    }
  },

  methods:{
    listaCelulasAtivas(linha, coluna){
      for (let c of this.celulasAtivas){
        if (c[0] === linha && c[1] === coluna) return true
      }

    }
  }
}
</script>

<style>

.quadrado{
  border: 0.5px grey solid;
  width: 15px;
  height: 15px;
  margin: 3px;
}

.flex{
  display: flex;
  box-sizing: border-box;
}
</style>
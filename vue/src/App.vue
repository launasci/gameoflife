<template>
  <div>
    <GameOfLife :iniciar-jogo="iniciar" />
    <button @click="iniciar = !iniciar"> Iniciar</button>
  </div>
    
</template>

<script>
import GameOfLife from './components/GameOfLife'

export default {
  name: 'App',
  components: {
    GameOfLife
  },

  data(){
    return{
    iniciar: false
   }
  }
}
</script>

<style>

</style>

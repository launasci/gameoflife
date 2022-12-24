<template>
  <MatrizCelulas  :colunas='10' :linhas='10' :celulas-ativas="celulasAtivas"/>
</template>

<script>
import gjs from "../helpers/gameoflife"
import MatrizCelulas from "./MatrizCelulas";

export default{
  components:{
    MatrizCelulas,
  },

  props:{
    iniciarJogo:{
      type: Boolean, 
      default: false
    }
  },

  watch:{
    iniciarJogo(v){
      this.gameOfLife()
    }
  },

  data(){
    return{
      celulasAtivas: this.randonRadint()
    }
  },
  
  methods:{
    randonRadint(){
      let listaCelulas = []
      for (let i = 0; i <= 40; i++){
        listaCelulas.push([Math.floor(Math.random()*10), Math.floor(Math.random()*10)])
      }
      console.log(listaCelulas)
      return listaCelulas
    },

    gameOfLife (){
      setInterval(()=>{
        if(this.celulasAtivas.length){
          this.celulasAtivas = gjs.updateCelulasVivas(this.celulasAtivas)
        }
      },1000)
    }
  }

}
</script>

<style>
</style>

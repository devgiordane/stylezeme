<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 text-center">
        <h1 class="h1  text-secondary">STYLEZEME</h1>
        <p class="lead">Gerador de fontes para textos</p>
      </div>
      <div class="col-12">
        <div class="form-group">
          <label for="">MENSAGEM</label>
          <textarea
            v-model="mensagem"
            rows="4"
            type="text"
            name=""
            id=""
            class="form-control"
          />
        </div>
      </div>
      <div
        class="col-12 d-flex align-items-baseline"
        v-for="(alfabeto, key) in alfabetos"
        :key="key"
      >
        <textarea
          class="form-control mb-3"
          type="text"
          :value="formatar(key)"
          :id="'texto' + key"
        />
        <button
          :data-clipboard-target="'#texto' + key"
          class="btn btnCopiar btn-primary btn-sm ml-3"
        >
          COPIAR
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import ClipboardJS from "clipboard";
// eslint-disable-next-line no-unused-vars
var clipboard = new ClipboardJS(".btnCopiar");

export default {
  name: "Gerador",
  data: function() {
    return {
      mensagem: "",
      alfabetos: [
        {
          a: "A",
          b: "B",
          c: "C",
          d: "D",
          e: "E",
          f: "F",
          g: "G",
          h: "H",
          i: "I",
          j: "J",
          k: "K",
          l: "L",
          m: "M",
          n: "N",
          o: "O",
          p: "P",
          q: "Q",
          r: "R",
          s: "S",
          t: "T",
          u: "U",
          v: "V",
          w: "W",
          x: "X",
          y: "Y",
          z: "Z"
        },
        {
          a: "𝓪",
          b: "𝓫",
          c: "𝓬",
          d: "𝓭",
          e: "𝓮",
          f: "𝓯",
          g: "𝓰",
          h: "𝓱",
          i: "𝓲",
          j: "𝓳",
          k: "𝓴",
          l: "𝓵",
          m: "𝓶",
          n: "𝓷",
          o: "𝓸",
          p: "𝓹",
          q: "𝓺",
          r: "𝓻",
          s: "𝓼",
          t: "𝓽",
          u: "𝓾",
          v: "𝓿",
          w: "𝔀",
          x: "𝔁",
          y: "𝔂",
          z: "𝔃"
        },
        {
          a: "𝕒",
          b: "𝕓",
          c: "𝕔",
          d: "𝕕",
          e: "𝕖",
          f: "𝕗",
          g: "𝕘",
          h: "𝕙",
          i: "𝕚",
          j: "𝕛",
          k: "𝕜",
          l: "𝕝",
          m: "𝕞",
          n: "𝕟",
          o: "𝕠",
          p: "𝕡",
          q: "𝕢",
          r: "𝕣",
          s: "𝕤",
          t: "𝕥",
          u: "𝕦",
          v: "𝕧",
          w: "𝕨",
          x: "𝕩",
          y: "𝕪",
          z: "𝕫"
        },
        {
          a: "🄰",
          b: "🄱",
          c: "🄲",
          d: "🄳",
          e: "🄴",
          f: "🄵",
          g: "🄶",
          h: "🄷",
          i: "🄸",
          j: "🄹",
          k: "🄺",
          l: "🄻",
          m: "🄼",
          n: "🄽",
          o: "🄾",
          p: "🄿",
          q: "🅀",
          r: "🅁",
          s: "🅂",
          t: "🅃",
          u: "🅄",
          v: "🅅",
          w: "🅆",
          x: "🅇",
          y: "🅈",
          z: "🅉"
        }
      ]
    };
  },
  methods: {
    formatar: function(key) {
      let texto = [];
      for (let letra = 0; letra < this.mensagem.length; letra++) {
        const l = this.mensagem[letra].toLowerCase();
        if (this.alfabetos[key][l] != undefined) {
          texto.push(this.alfabetos[key][l]);
        } else {
          texto.push(l);
        }
      }
      return texto.join("");
    }
  }
};
</script>

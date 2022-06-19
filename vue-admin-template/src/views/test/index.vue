<template>
  <div>
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose">
      <span>{{ this.tokenin }}</span>
      <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
      <el-button
      type="primary"
      style="margin-left: 20px"
      @click="Showtoken(); dialogVisible = true"
      >显示Token</el-button>
</div>
</template>

<script>
import {
  show_token
} from "@/api/tok";

export default {
  data() {
    return {
      name: "index",
      tokenin: '',
      dialogVisible: false,
    };
  },
  created() {
    console.log("here is nothing");
  },
  mounted() {
  },
  methods: {
    Showtoken() {
      show_token().then((res) => {
        // console.log("This is token")
        this.tokenin = res.token;
        console.log(this.tokenin);
      })
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
        })
        .catch(_ => {
        });
    },
  }
}
</script>



<style  scoped>
</style>

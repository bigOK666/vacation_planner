<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h2> AI 开启梦幻之旅 </h2>
                <form>
                    <div class="form-group">
                        <label for="current_location">所在地</label>
                        <input v-model="form.current_location" class="form-control" id="current_location" placeholder="current location"/>
                    </div>
                    <div class="form-group">
                        <label for="destination">目的地</label>
                        <input v-model="form.destination" class="form-control" id="destination" placeholder="destination"/>
                    </div>
                    <div class="form-group">
                        <label for="duration">旅行时长（天）</label>
                        <input v-model="form.duration" class="form-control" id="duration"/>
                    </div>
                    <div class="form-group">
                        <label for="budget">预算（元）</label>
                        <input v-model="form.budget" class="form-control" id="budget"/>
                    </div>
                </form>
        
                <div class="text-center">
                    <button type="button" class="btn btn-primary" @click="handleSubmit">免费规划</button>
                </div>
            </div>
            <div class="col">
                <div v-html="msg"></div>
            </div>
        </div>
    </div>
        
</template>

<script>
import axios from 'axios';
import Nprogress from 'nprogress';
import "nprogress/nprogress.css";



export default{
    name: 'VacationPlan',
    data(){
        return {
            msg:'',
            form:{
                current_location:'',
                destination:'',
                duration:0,
                budget:0,
            },
        };
    },

    methods:{
        handleSubmit(){
            const payload={
                current_location:this.form.current_location,
                destination:this.form.destination,
                duration:this.form.duration,
                budget:this.form.budget
            };
            this.submitForm(payload);
            this.initForm();
        },

        submitForm(payload){
            const path = 'http://localhost:5001/vacation-plan';
            Nprogress.start();
            axios.post(path, payload).then((res)=>{
                this.msg = res.data;
                Nprogress.done();
            }).catch((error)=>{
                console.error(error);
                this.msg = "Something went wrong";
                Nprogress.done();
            });
        },

        initForm(){
            this.form.current_location='',
            this.form.destination='',
            this.form.duration=0,
            this.form.budget=0
        }
    }
}
</script>
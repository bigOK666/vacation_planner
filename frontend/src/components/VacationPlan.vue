<template>
    <div class="container">
        <form>
            <div class="form-group">
                <label for="destination">Destination</label>
                <input v-model="form.destination" class="form-control" id="destination" placeholder="destination"/>
            </div>
            <div class="form-group">
                <label for="duration">Duration</label>
                <input v-model="form.duration" class="form-control" id="duration" placeholder="duration"/>
            </div>
            <div class="form-group">
                <label for="budget">Budget</label>
                <input v-model="form.budget" class="form-control" id="budget" placeholder="budget"/>
            </div>
            <button type="button" class="btn btn-primary" @click="handleSubmit">Submit</button>
        </form>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name: 'VacationPlan',
    data(){
        return {
            msg:'',
        };
    },
    methods:{
        handleSubmit(){
            const payload={
                destination:this.form.destination,
                duration:this.form.duration,
                budget:this.form.budget
            };
            this.submitForm(payload);
        },

        submitForm(payload){
            const path = 'http://localhost:5001/vacation-plan';
            axios.post(path, payload).then((res)=>{
                this.msg = res.data;
            }).catch((error)=>{
                console.error(error);
            });
        },
    }
}
</script>
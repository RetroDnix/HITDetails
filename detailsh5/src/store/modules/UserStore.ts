import { defineStore } from "pinia";
import { axiosInstance } from "@/utils/Axios";

const uStore = defineStore('userStore', {
    state: () => {
        return {
            userName: '',
            UID: 0,
            isloading: false,
            upToDate: false,
        }
    },
    actions: {
        async reloadAll() {
            if (this.isloading) return
            if (this.upToDate) return
            this.isloading = true
            try {
                const response = await axiosInstance.get("/user/username");
                this.UID = response.data.UID;
                this.userName = response.data.Name;
            }
            catch (error) {
                console.log(error);
            }
            this.isloading = false;
            this.upToDate = true;
        },
    }
})

export default uStore;
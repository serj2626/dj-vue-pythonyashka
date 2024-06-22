import ButtonBack from "./ButtonBack.vue";
import AlertMessage from "./AlertMessage.vue";


const components = [
    { name: "ButtonBack", component: ButtonBack },
    { name: "AlertMessage", component: AlertMessage }
];



export default {
    install(app) {
        components.forEach(({ name, component }) => {
            app.component(name, component);
        });
    },
};
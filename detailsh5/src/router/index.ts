// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('/src/views/HomePage.vue'),
  },
  {
    path: '/Bind',
    name: 'Bind',
    component: () => import('/src/views/BindPage.vue'),
  },
  {
    path: '/Help',
    name: 'Help',
    component: () => import('/src/views/HelpPage.vue'),
  },
  {
    path: '/Schedule',
    name: 'Schedule',
    component: () => import('/src/views/ScheduleTable.vue'),
  },
  {
    path: '/Schedule/createNewSchedule',
    name: 'createNewSchedule',
    component: () => import('/src/components/ScheduleDetail.vue'),
  },
  {
    path: '/ScheduleDetail/:id',
    name: 'ScheduleDetail',
    component: () => import('/src/components/ScheduleDetail.vue'),
  },
  {
    path: '/Group',
    name: 'Group',
    component: () => import('/src/views/Group.vue'),
  },
  {
    path: '/GroupDetail/:id',
    name: 'GroupDetail',
    component: () => import('/src/components/GroupDetail.vue'),
  },
  {
    path: '/Notification',
    name: 'Notification',
    component: () => import('/src/views/NotificationTable.vue'),
  },
  {
    path: '/Notification/:id',
    name: 'MessageDetail',
    component: () => import('/src/components/MessageDetail.vue'),
  },
  {
    path: '/Schedule/createNewMessage',
    name: 'createNewMessage',
    component: () => import('/src/components/MessageDetail.vue'),
  },
  {
    path: '/User',
    name: 'user',
    component: () => import('/src/views/User.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
    if (to.path == '/' || to.path == '/Bind' || to.path == '/Help')
    {
      next();
      return;
    }
    if (localStorage.getItem('Authorization') != null) { // 使用Vuex的getters检查用户是否已登录
      next();
    } else {
      alert('请先登录!');
      next({ path: '/' });
    }
});

export default router

import { createRouter, createWebHashHistory } from "vue-router";
import HelloWorld from "@/components/HelloWorld";
// import App from './App.vue'
import TestCase from '@/components/TestCase'
import Login from '@/components/Login'
import DataItem from '@/components/DataItem'
import DataTable from '@/components/DataTable'
import GitImport from '@/components/GitImport'
import Task from '@/components/Task'
import TaskList from '@/components/TaskList'

const routes = [
    {
        path: '/',
        component: Login
    },
    {
        path: '/hello',
        component: HelloWorld
    },
    {
        path: '/testcase',
        component: TestCase,
        children:[
            {
                path: 'all',
                component: DataTable
            },
            {
                path: 'edit',
                component: DataItem
            },
            {
                path: 'import',
                component: GitImport
            },

        ]
    },

    {
        path: '/task',
        component: Task,
        children:[
            {
                path: 'all',
                component: TaskList
            },
            {
                path: 'edit',
                component: DataItem
            },
            {
                path: 'import',
                component: GitImport
            },

        ]
    },
    
    {
        path: '/login',
        component: Login
    },

    // { path: '/about', component: About },
]

const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})

export default router
import { configureStore } from "@reduxjs/toolkit";

import authReducer from "./features/authSlice";


/*  a reducer is basically just a function that takes
    in an action and the previous state of the application
    and makes the changes to that state based on the actions
    and return updated state.
*/
export const store = configureStore({
    reducer: {
        authReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

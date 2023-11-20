import { createAsyncThunk ,createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
// import {login} from "../../server-actions/auth/login";


type InitialState = {
    value: AuthState;
}

type AuthState = {
    isAuth: boolean;
    username: string;
}

interface MyAction extends PayloadAction<{
    email: string;
    password: string;
}> {}

const initialState = {
    value: {
        isAuth: false,
        username: "",
    } as AuthState,
} as InitialState;

const fetchAuth = createAsyncThunk(
    'auth/fetchAuthCred',
    async (data:any) => {
        const {email, password} = data
        try {
            // login(email, password)
            console.log("work till here.")

        } catch (error) {
            console.log(error)
        }

    }
)


export const auth = createSlice({
    name: "auth",
    initialState,
    reducers: {
        logIn: (state, action: MyAction) => {

        },
        logOut: () => {
            return initialState;
        },
    },
    extraReducers: (builder) => {
        builder.addCase(fetchAuth.fulfilled, (state, action) => {

        })
    }
})

// export const {logIn, logOut} = auth.actions;
export const authActions = {
    ...auth.actions,
    fetchAuth
}
export default auth.reducer;

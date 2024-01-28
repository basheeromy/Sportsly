import { createAsyncThunk ,createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { loginAction } from "@/server-actions/auth/login";


type InitialState = {
    value: AuthState;
}

type AuthState = {
    isAuth: boolean;
    username: string;
}

const initialState = {
    value: {
        isAuth: false,
        username: "",
        id:"",
    } as AuthState,
} as InitialState;

const fetchAuth = createAsyncThunk(
    'auth/fetchAuthCred',
    async (data:any) => {
        try {
            console.log("work till here.")
            loginAction(data)

        } catch (error) {
            console.log(error)
        }

    }
)


export const auth = createSlice({
    name: "auth",
    initialState,
    reducers: {
        logOut: () => {
            return initialState;
        },
    },
    extraReducers: (builder) => {
        builder.addCase(fetchAuth.fulfilled, (state, action) => {

        })
    }
})


export const authActions = {
    ...auth.actions,
    fetchAuth
}
export default auth.reducer;

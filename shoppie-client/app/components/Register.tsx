
"use client"
import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { RegisterData, Gender } from "../interface";
import axios from 'axios'
import register from "../services/commonServices";
import axiosInstance from "../services/interceptor";

const Register: React.FC = () => {
    const {
        register,
        watch,
        handleSubmit,
        formState: { errors },
    } = useForm<RegisterData>();

    const [show, setShow] = useState(false);
    const formData = watch();
    const formSubmit = async (data: RegisterData) => {
 
        try {
            console.log("axios instance>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", axiosInstance);
            const response = await axiosInstance.post("customers/register", data) 
            console.log("respoonse ", response.data);
            
            setShow(true);
        } catch (error) {
            console.log(error);
        }
    }


    return (
        <div >
            <section className=" min-w-40 ">
                <div className="flex flex-col w-full items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 min-w-[30rem]">
                    <a
                        href="#"
                        className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
                    >
                        <img
                            className="w-8 h-8 mr-2"
                            src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg"
                            alt="logo"
                        />
                        Flowbite
                    </a>
                    <div className="w-full  rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:border-gray-700">
                        <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
                            <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                                Sign in to your account
                            </h1>
                            <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit(formSubmit)}>
                                <div className="lg:flex gap-2">

                                    <div>
                                        <label
                                            htmlFor="first_name"
                                            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                        >
                                            First Name
                                        </label>
                                        <input
                                            {...register("first_name", { required: true })}
                                            type="text"
                                            name="first_name"
                                            id="first_name"
                                            className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                            placeholder="First Name"
                                            required
                                        />
                                        {errors.first_name && <span>This field is required</span>}
                                    </div>
                                    <div>
                                        <label
                                            htmlFor="last_name"
                                            className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                        >
                                            Last Name
                                        </label>
                                        <input
                                            {...register("last_name", { required: true })}
                                            type="text"
                                            name="last_name"
                                            id="last_name"
                                            className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                            placeholder="Last Name"
                                            required
                                        />
                                        {errors.last_name && <span>This field is required</span>}
                                    </div>
                                </div>
                                <div>
                                    <label
                                        htmlFor="email"
                                        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Your email
                                    </label>
                                    <input
                                        {...register("email", { required: true })}
                                        type="email"
                                        name="email"
                                        id="email"
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="name@company.com"
                                        required
                                    />
                                    {errors.email && <span>This field is required</span>}
                                </div>
                                <div className="lg:flex gap-2 ">

                                <div className="w-full">
                                    <label
                                        htmlFor="dob"
                                        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Date of Birth
                                    </label>
                                    <input
                                        {...register("dob", { required: true })}
                                        type="date"
                                        name="dob"
                                        id="dob"
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        required
                                    />
                                    {errors.dob && <span>This field is required</span>}
                                </div>
                                <div className="w-full">
                                    <label
                                        htmlFor="gender"
                                        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Gender
                                    </label>
                                    <select
                                        {...register("gender", { required: true })}
                                        name="gender"
                                        id="gender"
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        required
                                    >
                                        <option value={Gender.Male}>Male</option>
                                        <option value={Gender.Female}>Female</option>

                                    </select>
                                    {errors.gender && <span>This field is required</span>}
                                </div>
                                </div>
                                <div>
                                    <label
                                        htmlFor="address"
                                        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Address
                                    </label>
                                    <textarea
                                        {...register("address", { required: true })}
                                      typeof="address"
                                        name="address"
                                        id="address"
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        placeholder="Your address"
                                        required
                                    />
                                    {errors.address && <span>This field is required</span>}
                                </div>
                                <div>
                                    <label
                                        htmlFor="password"
                                        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                                    >
                                        Password
                                    </label>
                                    <input
                                        {...register("password", { required: true })}
                                        type="password"
                                        name="password"
                                        id="password"
                                        placeholder="••••••••"
                                        className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                        required
                                    />
                                    {errors.password && <span>This field is required</span>}
                                </div>
                                <button
                                    type="submit"
                                    className="w-full  bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
                                >
                                    Sign in
                                </button>
                                <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                                    Don’t have an account yet?{" "}
                                    <a
                                        href="#"
                                        className="font-medium text-primary-600 hover:underline dark:text-primary-500"
                                    >
                                        Sign up
                                    </a>
                                </p>
                            </form>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Register;

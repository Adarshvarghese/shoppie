export enum Gender{
    Male = 1,
    Female = 2,
}

export interface RegisterData{
    first_name: string;
    last_name: string;
    email: string;
    dob : string;
    gender : Gender;
    address: string;
    password: string;
}


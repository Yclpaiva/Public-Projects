import { getListIndustriesFromDB } from '../repositories/dbRepositories';

let count = 0;

export const serviceListIndustries = async () => {
    try {
        const industries = await getListIndustriesFromDB();
        console.log("Industries consult successful");
        count++;
        console.log(`Industries consult count: ${count}`);
        return industries;
    } catch (error) {
        console.error('Error fetching industries:', error);
        throw error;
    }
};

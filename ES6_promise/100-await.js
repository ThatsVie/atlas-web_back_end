import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const photo = await uploadPhoto();
    const user = await createUser();
    return { photo, user };
  } catch (error) {
    // If an error occurs in either uploadPhoto or createUser, return null for both
    return { photo: null, user: null };
  }
}

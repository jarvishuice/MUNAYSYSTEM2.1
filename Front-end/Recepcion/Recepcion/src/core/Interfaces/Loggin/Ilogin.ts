import { UsersEntity } from "../../Entities/users/userEntity";

export abstract class Iloggin{
abstract  logout(user:UsersEntity):Promise<boolean>;


}
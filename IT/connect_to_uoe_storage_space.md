# Connecting to the UoE shared storage from Ubuntu

## Mounting

In the following, ``csce`` is your college name and may vary with users

```
sudo apt-get install cifs-utils
mkdir /mnt/uoe_shared_folder
sudo mount.cifs //csce.datastore.ed.ac.uk/[path/to/shared] /mnt/uoe_shared_folder -o user=[username]@ed.ac.uk
```

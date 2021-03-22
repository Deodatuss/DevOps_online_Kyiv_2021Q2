## PART 1. HYPERVISORS
1. Oracle VM, Azure Virtual Machines, Hyper-V and vSphere
2. Hyper-V is known for effecive hardware use, vSphere includes such additional features as management and interface layers, and Azure VM is a cloud service which provides hardware and gives flexibility of virualisation

## PART 2. WORK WITH VIRTUALBOX
Downloaded and ran VirtualBox. Made two VMs, second is a clone of the first. 
![Made a Clone](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_1Q8LgKPRUE.png)

Created group of two VMs. Made Snapshots branch
![Snapshots](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_oLlI8VLrx4.png)

exported first VM
![export](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/explorer_UaM33VKDuH.png)

Explored VM configuration options
![Display](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_FUd7YW3ZzH.png)

Configured the USB to connect to the VM
![USB](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_JIuQkpY4wt.png)

Configured a shared folder between host and VM
![Shared folders](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_U6CzOyZ6e9.png)

Configured different network modes for VM1 and VM2(cloned VM1)
![Network](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_15Ux9DUrXD.png)
![Clone network](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/VirtualBox_lnppgi1G2R.png)


Used CLI with VBoxManage. Examined the purpose of basic VBoxManage commands
![CLI 1](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/cmd_DBpWx74vp7.png)
![CLI 2](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/cmd_nTgTyOXbyM.png)

## PART 3. WORK WITH VAGRANT
Made folder vagrant_test, initialized default Vagrant box with `init hashicorp/precise64`. Ran `vagrant up` to boot VM
![init hashicorp/precise64](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/powershell_6nY1rOOUaF.png)

Used PuTTY to connect to the made VM. Executed `date` command to record precise date & time
![PuTTY](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/putty_CAxFbNND6k.png)

Deleted VM
![Delete Vagrant VM](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/powershell_U7zWEuYN1b.png)

And made Vagrant box
![Vagrant box](https://github.com/Deodatuss/DevOps_online_Kyiv_2021Q2/blob/main/m2/task2.1/screenshots/powershell_HDA4Rr1Dsa.png)


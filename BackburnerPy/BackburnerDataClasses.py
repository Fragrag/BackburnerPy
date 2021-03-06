from dataclasses import dataclass
import ipaddress

@dataclass
class NetworkStatus:
    """Backburner Manager network status
    
    Attributes:
        dropped_packets (int)
        bad_packets (int)
        tcp_requests (int)
        udp_requests (int)
        boot_time (str)

    """
    dropped_packets: int
    bad_packets: int
    tcp_requests: int
    udp_requests: int
    boot_time: str

@dataclass
class SystemInfo:
    """Backburner Manager system information
    
    Attributes:

        total_memory (int)
        total_memory_f (float)
        num_cpus (int)
        platform (str)
        user (str)
        computer_name (str)
        mac (str)
        workdisk_space (int)
        ip_address (str)

    """
    total_memory: int
    total_memory_f: float
    num_cpus: int
    platform: str
    user: str
    computer_name: str
    mac: str
    workdisk_space: int
    ip_address: str

    def get_ipaddress_object(self):
        return ipaddress.ip_address(ip_address)

@dataclass
class HardwareInfo:
    """Backburner Manager hardware information
    
    Attributes:
        total_memory (int)
        total_memory_f (float)
        num_cpus (int)
        platform (str)
        workdisk_space (int)
        mac (str)

    """
    total_memory: int
    total_memory_f: float
    num_cpus: int
    platform: str
    workdisk_space: int
    mac: str

@dataclass
class BackburnerManagerInfo:
    """Backburner Manager information
    
    Attributes:
        version (int)
        servers (int)
        jobs (int)
        system_info (:obj:`SystemInfo`)
        network_status (:obj:`NetworkStatus`)

    """
    version: int
    servers: int
    jobs: int
    system_info: SystemInfo
    network_status: NetworkStatus

@dataclass 
class Client:
    """Client information
    
    Attributes:

        version (int)
        udp_port (int)
        controller (bool)
        system_info (:obj:`SystemInfo`)
    
    """
    version: int
    udp_port: int
    controller: bool
    system_info: SystemInfo

@dataclass
class Plugin:
    """Plugin information
    
    Attributes:
        version (int)
        name (str)
        description (str)

    """
    version: int
    name: str
    description: str

@dataclass
class JobArchiveListItem:
    """

    Attributes:
        handle (int)
        name (str)
        user (str)
        description (str)
        submission_date (str)
        end_job_date (str)
        plugin_name (str)
        plugin_version (int)
    """
    handle: int
    name: str
    user: str
    description: str
    submission_date: str
    end_job_date: str
    plugin_name: str
    plugin_version: int

@dataclass 
class JobHandleListItem:
    """Item in Job Handle List
    
    Attributes:
        handle (int)
        state (int)

    """
    handle: int
    state: int

@dataclass
class JobListItem:
    """Item in Job List

    Attributes:
        handle (int)
        state (int)
        name (str)
        plugin_name (str)
        plugin_version (int)

    """
    handle: int
    state: int
    name: str
    plugin_name: str
    plugin_version: int

@dataclass
class JobInfo:
    """Job information
    
    Attributes:
        version (int)
        handle (int)
        name (str)
        description (str)
        priority (int)
        user (str)
        computer (str)
        last_updated (str)
        submitted (str)
        started (str)
        ended (str)
        number_tasks (int)
        tasks_completed (int)
        encoding (str)

    """
    version: int
    handle: int
    name: str
    description: str
    priority: int
    user: str
    computer: str
    last_updated: str
    submitted: str
    started: str
    ended: str
    number_tasks: int
    tasks_completed: int
    encoding: str

@dataclass 
class JobFlags:
    """Job flags
    
    Attributes:
        active (bool)
        complete (bool)
        nonconcurrent (bool)
        nonstoppable (bool)
        ignore_job_share (bool)
        has_dependencies (bool)
        zip_archive (bool)
        leave_in_queue (bool)
        archive_when_done (bool)
        delete_when_done (bool)
        override_blocking_tasks (bool)
        enable_blocking_tasks (bool)

    """
    active: bool
    complete: bool
    nonconcurrent: bool
    nonstoppable: bool
    ignore_job_share: bool
    has_dependencies: bool
    zip_archive: bool
    leave_in_queue: bool
    archive_when_done: bool
    delete_when_done: bool
    override_blocking_tasks: bool
    enable_blocking_tasks: bool

@dataclass 
class JobPlugin:
    """Job plugin information
    
    Attributes:
        plugin_name (str)
        plugin_version (int)

    """
    plugin_name: str
    plugin_version: int

@dataclass
class JobAlerts:
    """Job alert settings
    
    Attributes:
        enabled (bool)
        failure (bool)
        progress (bool)
        completion (bool)
        nth_task (int)
        send_email (bool)
        include_summary (bool)
        email_from (str)
        email_to (str)
        email_server (str)
    
    """
    enabled: bool
    failure: bool
    progress: bool
    completion: bool
    nth_task: int
    send_email: bool
    include_summary: bool
    email_from: str
    email_to: str
    email_server: str

@dataclass
class JobServerList:
    """Job server list settings

    Attributes:
        all (bool)

    """
    all: bool

@dataclass
class JobServer:
    """Job server information
    
    Attributes:
        handle (str)
        active (bool)
        task_time (float)
        task_total (int)
        context_switch (int)
        rt_failed (bool)

    """
    handle: str
    active: bool
    task_time: float
    task_total: int
    context_switch: int
    rt_failed: bool

@dataclass 
class Job:
    """Job information
    
    Attributes:

        info (:obj:`JobInfo`)
        flags (:obj:`JobFlags`)
        plugin (:obj:`JobPlugin`)
        alerts (:obj:`JobAlerts`)
        servers (:obj:`list` of :obj:`JobServer`)
    
    """
    info: JobInfo
    flags: JobFlags
    plugin: JobPlugin
    alerts: JobAlerts
    servers: list

@dataclass
class ServerSchedule:
    """Server schedule

    Each day is assigned a 24 bit bytearray that is represented by an integer. Each bit in the array represents an hour in the day, starting from 00:00 till 23:00.

    To design a schedule, simply create a 24 bit bytearray, with 1s where the server is allowed to be active, and 0s when the server has to be inactive. 
    The following example is the server's setting for a day where the computer is inactive during office hours, i.e. from 07:00 till 18:00:

    - Binary: 111111100000000000111111
    - Decimal: 16646207
    
    Attributes:

        sunday (int)
        monday (int)
        tuesday (int)
        wednesday (int)
        thursday (int)
        friday (int)
        saturday (int)

    """
    sunday: int
    monday: int
    tuesday: int
    wednesday: int
    thursday: int
    friday: int
    saturday: int

@dataclass
class ServerListItem:
    """Server item in list
    
    Attributes:
        handle (str)
        state (int)
        name (str)

    """
    handle: str
    state: int
    name: str

@dataclass 
class Server:
    """Server information
    
    Attributes:
        version (int)
        name (str)
        user_name (str)
        total_task (int)
        total_time (float)
        perf_index (float)
        ip_address (str)
        current_status (int)
        hw_info (:obj:`HardwareInfo`)
        network_status (:obj:`NetworkStatus`)
        server_schedule (:obj:`ServerSchedule`)
        att_priority (bool)
        una_priority (bool)
        current_job (int)
        current_task (int)
        task_started (str)
        plugins (:obj:`list` of :obj:`Plugin`)

    """
    version: int
    name: str
    user_name: str
    total_task: int
    total_time: float
    perf_index: float
    ip_address: str
    current_status: int
    hw_info: HardwareInfo
    network_status: NetworkStatus
    server_schedule: ServerSchedule
    att_priority: bool
    una_priority: bool
    current_job: int #TODO: Check this, it might also be a hex string
    current_task: int
    task_started: str
    plugins: list

    def get_ipaddress_object(self):
        return ipaddress.ip_address(ip_address)

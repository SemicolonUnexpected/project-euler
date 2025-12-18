const std = @import("std");

pub fn main() !void {
    var sum: u64 = 0;
    for (0..999) |num| {
        if (num % 3 == 0 or num % 5 == 0) {
            sum += num;
        }
    }
    std.debug.print("Sum is {}\n", .{sum});
}
